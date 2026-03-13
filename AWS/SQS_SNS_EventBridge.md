# SQS | SNS | Event Bridge

([Link](https://www.youtube.com/watch?v=RoKAEzdcr7k))

**SQS**

- Simple queue service (old)
- application owners to publish message to queue
- 1) queue 2) message 3) polling
    - 1) fifo where you just publish 2) message - any blob (json) 3) polling - applications that subscribe will “poll”
- ex. ecommerce
    
    - “service (subscriber) creates a queue”
    - lambda function will automatically poll if implemented with sqs
    - **need to configure queue to be fifo when creating**

**SNS (multiple subscribers - more scalable architecture than 3x sqs)**

- Simple notification service (old)
- 1) topics 2) messages 3) publish/ subscribe (aka PubSub)
- topic is not a holding pool  - message enters and leaves
- ex.
    
    
    - SNS (As long as subscription set of for the topic)
        - will send the message

        
    - generally not good for SNS subscribe to an end point
        - they normally put queue between

**Event Bridge (new)**

- similar to SNS, improvements, changes
- 1) message bus 2) events 3) rules 4) targets
- message bus - topic | events - compatible with other aws service, SAAS, etc | rules - match coming message and output |
    - message filtering
- diagram is the same as as SNS

- with event bridge
    - the advantage is - 3rd party integration (should i do it then? or no)
- biggest problem
    - new and limitations
    - specific rule - 5 targets
- only triggers AWS

When to use what

- SQS
    - reliable 1:1 Async comm
    - temporary message holding pool
    - can configure ordered message processing
- SNS
    - 1 to many fanout (copy published to subscribers)
- EventBridge
    - 1 to many (with limitations)
    - AWS, SaS, or application integrations