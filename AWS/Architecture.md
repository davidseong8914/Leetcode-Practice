# Event Driven Architecture

**Event Driven Architecture in 7 Minutes ([Link](https://www.youtube.com/watch?v=gOuAqRaDdHA))**

- Producer (Event )→ Broker (distributes Events) → consumer (services events)

- Event - information on what happened by who
    - immutable - permanent
- Event Broker - reads event and sends to subscribed services

Processes can be run separately (Back end, data processing)

Advantages over API 

- decouples components (independent publisher, consumer,
    - ex. api: inter dependent (one goes down, both goes down)
- able to upgrade a component without ruining anything
- scalable - since decoupled, add components infinitely

Disadvantages

- Data consistency - delay between publish and subscription
- more complex - more components needs to be built
- harder to debug

if we are not scaling yet, may not be worth the effort




**Event Driven Architecture vs Workflows (with AWS Services!) ([Link](https://www.youtube.com/watch?v=Q_QCu6OP2mQ))**

**Event Based Architecture (Choreography)**

- AWS services
    - Lambda function = connector? - does something
    - SNS topic - broadcast message?
    - SQS queues?
    - Dynamo DB
    - IOT
- Advantage
    - decentralization
        - linking is what does the processing
        - can distribute work more easily
    - performance
        - no centralized coordinator
- Disadvantage
    - Monitoring - hard to tell where the process is
    - Failure handling
        - ex. process fails at credit card service
        - rewind and undo
        - build additional logic to handle failure scenarios

**Workflows (Orchestrator) - centralized commander**


- Sequence step functions
    
- Benefits:
    - centralization of workflow
        - workflow is easy to monitor
        - explicit failure states
- cons:
    - step function is not free
    - difficult to separate work loads/ independent component for separate teams