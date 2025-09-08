#!/usr/bin/env python3
import os, re, csv, json
from datetime import datetime, timedelta

CSV_FILE = "lc75_list.csv"
MD_OUT = "dashboard.md"
HTML_OUT = "dashboard.html"

def load_problem_list(csv_file):
    problems = []
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            if not row or row[0].strip().startswith("#"):
                continue
            if len(row) < 2:
                pid = row[0].strip()
                title = ",".join(row[1:]).strip()
            else:
                pid, title = row[0].strip(), row[1].strip()
            if pid and title:
                problems.append({"id": pid, "title": title})
    return problems

def parse_attempted_ids():
    attempted = set()
    date_set = set()
    digit_prefix = re.compile(r"^(\d+)_")
    date_pat = re.compile(r"_(\d{8})")
    for fname in os.listdir("."):
        if os.path.isdir(fname):
            continue
        m = digit_prefix.match(fname)
        if m:
            attempted.add(m.group(1))
        dm = date_pat.search(fname)
        if dm:
            ymd = dm.group(1)
            try:
                dt = datetime.strptime(ymd, "%Y%m%d").date()
                date_set.add(dt.isoformat())
            except ValueError:
                pass
    return attempted, sorted(date_set)

def compute_streaks(date_strs):
    if not date_strs:
        return {"current_streak": 0, "best_streak": 0, "most_recent_day": None}
    dates = sorted({datetime.strptime(s, "%Y-%m-%d").date() for s in date_strs})
    best = 1
    cur = 1
    most_recent = dates[-1]
    for i in range(1, len(dates)):
        prev = dates[i-1]
        today = dates[i]
        if (today - prev).days == 1:
            cur += 1
        else:
            best = max(best, cur)
            cur = 1
    best = max(best, cur)
    return {
        "current_streak": cur,
        "best_streak": best,
        "most_recent_day": most_recent.isoformat()
    }

def write_markdown(problems, attempted_ids, streak_info, md_path):
    total = len(problems)
    attempted_count = sum(1 for p in problems if p["id"] in attempted_ids)
    header = [
        "# LeetCode 75 Dashboard",
        "",
        f"- **Total problems:** {total}",
        f"- **Attempted:** {attempted_count}/{total}",
        f"- **Current streak:** {streak_info['current_streak']} day(s)",
        f"- **Best streak:** {streak_info['best_streak']} day(s)",
        f"- **Most recent solve day:** {streak_info['most_recent_day'] or '—'}",
        "",
        "Edit the table below for columns 3–6 as you progress.",
        ""
    ]
    lines = header + [
        "| # | Title | Attempted | First Try Pass | Passed Eventually | Optimal | Thoughts |",
        "|---|-------|-----------|----------------|-------------------|---------|----------|",
    ]
    for p in problems:
        att = "O" if p["id"] in attempted_ids else "X"
        lines.append(f"| {p['id']} | {p['title']} | {att} |  |  |  |  |")
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def render_row(problem, attempted):
    att = "O" if attempted else "X"
    # Use {{ and }} to escape literal braces for Python .format
    return """
      <tr data-pid="{pid}">
        <td>{pid}</td>
        <td>{title}</td>
        <td class="attempted {att}">{att}</td>
        <td class="editable" contenteditable="true" data-field="first_try"></td>
        <td class="editable" contenteditable="true" data-field="passed"></td>
        <td class="editable" contenteditable="true" data-field="optimal"></td>
        <td class="editable" contenteditable="true" data-field="thoughts"></td>
      </tr>
    """.format(pid=problem['id'], title=problem['title'], att=att)



def write_html(problems, attempted_ids, streak_info, html_path):
    from string import Template
    rows_html = "".join(render_row(p, (p['id'] in attempted_ids)) for p in problems)
    template_text = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>LeetCode 75 Dashboard</title>
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Ubuntu, Cantarell, Noto Sans, "Helvetica Neue", Arial, "Apple Color Emoji", "Segoe UI Emoji"; margin: 24px; }
    h1 { margin-bottom: 0.25rem; }
    .muted { color: #666; }
    table { border-collapse: collapse; width: 100%; margin-top: 1rem; }
    th, td { border: 1px solid #ddd; padding: 8px; vertical-align: top; }
    th { background: #f7f7f7; text-align: left; }
    tr:nth-child(even) { background: #fafafa; }
    .pill { display:inline-block; padding:2px 8px; border-radius:999px; background:#efefef; margin-right:8px; }
    .attempted.O { background:#e6ffed; }
    .attempted.X { background:#ffecec; }
    .editable { background: #fffef6; min-width: 90px; }
    .sticky-head th { position: sticky; top: 0; background: #f7f7f7; z-index: 1; }
    .toolbar { display:flex; gap:8px; align-items:center; flex-wrap: wrap; }
    button { padding: 6px 10px; border: 1px solid #aaa; background: #fff; cursor: pointer; border-radius: 6px; }
    button:hover { background:#f2f2f2; }
    .search { padding:6px 10px; border:1px solid #aaa; border-radius:6px; min-width: 220px; }
  </style>
</head>
<body>
  <h1>LeetCode 75 Dashboard</h1>
  <div class="muted">
    <span class="pill">Total: $TOTAL</span>
    <span class="pill">Attempted: $ATTEMPTED/$TOTAL</span>
    <span class="pill">Current streak: $CUR_STREAK</span>
    <span class="pill">Best streak: $BEST_STREAK</span>
    <span class="pill">Most recent day: $RECENT</span>
  </div>

  <div class="toolbar" style="margin-top:12px;">
    <input id="q" class="search" type="search" placeholder="Filter by id or title…" oninput="filterRows()">
    <button onclick="clearAllNotes()">Clear Notes (Cols 3–6)</button>
    <button onclick="exportNotes()">Export Notes (JSON)</button>
    <input type="file" id="importFile" accept="application/json" onchange="importNotes(event)" />
  </div>

  <table id="grid">
    <thead class="sticky-head">
      <tr>
        <th style="width:90px;">#</th>
        <th>Title</th>
        <th style="width:110px;">Attempted</th>
        <th style="width:130px;">First Try Pass</th>
        <th style="width:140px;">Passed Eventually</th>
        <th style="width:110px;">Optimal</th>
        <th>Thoughts</th>
      </tr>
    </thead>
    <tbody>
      $ROWS
    </tbody>
  </table>

<script>
function keyFor(id, field) { return `lc75::${id}::${field}`; }

function saveCell(e) {
  const td = e.target;
  const id = td.closest('tr').dataset.pid;
  const field = td.dataset.field;
  localStorage.setItem(keyFor(id, field), td.innerText.trim());
}

function loadCells() {
  document.querySelectorAll('tbody tr').forEach(tr => {
    const id = tr.dataset.pid;
    ['first_try','passed','optimal','thoughts'].forEach(field => {
      const key = keyFor(id, field);
      const val = localStorage.getItem(key);
      if (val !== null) {
        const cell = tr.querySelector(`[data-field="${field}"]`);
        if (cell) cell.innerText = val;
      }
    });
  });
}

function clearAllNotes() {
  if (!confirm('Clear all saved notes for columns 3–6?')) return;
  document.querySelectorAll('tbody tr').forEach(tr => {
    const id = tr.dataset.pid;
    ['first_try','passed','optimal','thoughts'].forEach(field => {
      localStorage.removeItem(keyFor(id, field));
      const cell = tr.querySelector(`[data-field="${field}"]`);
      if (cell) cell.innerText = '';
    });
  });
}

function exportNotes() {
  const data = {};
  document.querySelectorAll('tbody tr').forEach(tr => {
    const id = tr.dataset.pid;
    data[id] = {
      first_try: localStorage.getItem(keyFor(id, 'first_try')) || '',
      passed: localStorage.getItem(keyFor(id, 'passed')) || '',
      optimal: localStorage.getItem(keyFor(id, 'optimal')) || '',
      thoughts: localStorage.getItem(keyFor(id, 'thoughts')) || '',
    };
  });
  const blob = new Blob([JSON.stringify(data, null, 2)], {type:'application/json'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'lc75_notes.json';
  a.click();
  URL.revokeObjectURL(url);
}

function importNotes(evt) {
  const file = evt.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = e => {
    try {
      const data = JSON.parse(e.target.result);
      Object.entries(data).forEach(([id, vals]) => {
        ['first_try','passed','optimal','thoughts'].forEach(field => {
          const val = vals[field] || '';
          localStorage.setItem(keyFor(id, field), val);
        });
      });
      loadCells();
      alert('Notes imported ✅');
    } catch (err) {
      alert('Failed to import JSON: ' + err);
    }
  };
  reader.readAsText(file);
}

function filterRows() {
  const q = document.getElementById('q').value.toLowerCase();
  document.querySelectorAll('#grid tbody tr').forEach(tr => {
    const text = tr.innerText.toLowerCase();
    tr.style.display = text.includes(q) ? '' : 'none';
  });
}

document.addEventListener('input', function(e) {
  if (e.target.matches('.editable')) saveCell(e);
});

document.addEventListener('DOMContentLoaded', loadCells);
</script>
</body>
</html>
"""
    # Escape JS template literals like ${id} so Python's Template ignores them.
    template_text = template_text.replace("${", "$${")
    html = Template(template_text).substitute(
        TOTAL=len(problems),
        ATTEMPTED=sum(1 for p in problems if p['id'] in attempted_ids),
        CUR_STREAK=streak_info['current_streak'],
        BEST_STREAK=streak_info['best_streak'],
        RECENT=streak_info['most_recent_day'] or '—',
        ROWS=rows_html
    )
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
def main():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            w.writerow(["# Put your LeetCode 75 list here as id,title"])
            w.writerow(["1768","Merge Strings Alternately"])
            w.writerow(["1071","Greatest Common Divisor of Strings"])
            w.writerow(["1431","Kids With the Greatest Number of Candies"])
        print(f"[!] {CSV_FILE} not found. A starter file has been created.")
        print("    Please fill it with the exact LeetCode 75 list (id,title) and rerun.")
        return

    problems = load_problem_list(CSV_FILE)
    attempted_ids, date_strs = parse_attempted_ids()
    streak_info = compute_streaks(date_strs)
    write_markdown(problems, attempted_ids, streak_info, MD_OUT)
    write_html(problems, attempted_ids, streak_info, HTML_OUT)
    print(f"[✓] Generated {MD_OUT} and {HTML_OUT}")
    print(f"    Attempted: {sum(1 for p in problems if p['id'] in attempted_ids)}/{len(problems)}")
    if streak_info['most_recent_day']:
        print(f"    Current streak: {streak_info['current_streak']} | Best streak: {streak_info['best_streak']} | Most recent: {streak_info['most_recent_day']}")

if __name__ == "__main__":
    main()
