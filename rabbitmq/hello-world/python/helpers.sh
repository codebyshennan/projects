# use rabbitmqctl to list queues

# Usage: list_queues
list_queues() {
    rabbitmqctl list_queues name messages_ready messages_unacknowledged
}