# Linked List Notes

## General:
    - Linked series of nodes, each with:
        - data
        - reference to .next,
        - (and if it's a doubly linked list) reference to .previous
    - List itself has nodes linked, with 'head' and 'tail node
        - One person called to the "head" as the "seed"
        - 'tail' refers to the last node
            - BUT some people use the word 'tail' to refer to the entire post-head chain

### Pros:
    - Fast start/tail lookups
    - Flexible Size
### Cons:
    - Slow lookups
    - Not cache friendly (as nodes are not stored sequentially in memory)
