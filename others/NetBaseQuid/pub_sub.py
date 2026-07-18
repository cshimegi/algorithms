def broker():
    """Manages subscriptions and message distribution."""
    subscribers = []
    while True:
        message = yield  # Receive message from publisher
        # handle subscription/unsubscription
        if message and message[0] in ['subscribe', 'unsubscribe']:
            if isinstance(message, tuple): #we have a subscriber command
                if message[0] == 'subscribe':
                    subscribers.append(message[1])
                elif message[0] == 'unsubscribe' and message[1] in subscribers:
                    subscribers.remove(message[1])
            continue


        for subscriber in subscribers[:]: # make a copy to avoid modification during iteration
            try:
                subscriber.send(message)  # Send message to subscriber
            except StopIteration:
                subscribers.remove(subscriber) #remove subscriber if it is done.

def subscriber(name):
    """Receives and prints messages."""
    print(f"{name} subscribed.")
    try:
        while True:
            message = yield  # Receive message from broker
            print(f"{name} received: {message}")
    except GeneratorExit:
        print(f"{name} unsubscribed.")

def publisher(broker_gen, messages):
    """Sends messages to the broker."""
    try:
        for message in messages:
            broker_gen.send(message)
    except StopIteration:
        pass

# Setup
broker_gen = broker()
next(broker_gen)  # Prime the broker generator

subscriber1 = subscriber("Subscriber 1")
next(subscriber1)  # Prime the subscriber generator

subscriber2 = subscriber("Subscriber 2")
next(subscriber2)

broker_gen.send(('subscribe', subscriber1))
broker_gen.send(('subscribe', subscriber2))

publisher(broker_gen, ["Hello", "World", "Python", "Pub/Sub"])

broker_gen.send(('unsubscribe', subscriber2))

publisher(broker_gen, ["Only subscriber 1 will receive this"])

broker_gen.close()
subscriber1.close()
subscriber2.close()