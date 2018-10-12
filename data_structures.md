## Array
- **Description**: basic data structure, stored in one memory block.
- **Creation**: O(N)
- **Search**: O(N)
- **Insert**: O(N) (can be improved to O(1) by managing `capacity = Nx2`)
- **Delete**: O(N)

## List
- **Description**: basic data structure
- **Creation**: O(N)
- **Search**: O(N)
- **Insert**: O(N) (O(1) if position is known)
- **Delete**: O(N) (O(1) if position is known)

## Stack (LIFO)
- **Description**: structure with two operations: `push()` and `pop()`
- **Creation**: O(N)
- **Search**: n/a
- **Insert/push**: O(1)
- **Delete/pop**: O(1)
Base implementation is array-based.

## Queue (FIFO)
- **Description**: structure with two operations: `enqueue()` and `dequeue()`
- **Creation**: O(N)
- **Search**: n/a
- **Insert/enqueue**: O(1)
- **Delete/dequeue**: O(1)
Base implementation is list-based. Can be also implemented using two stacks.

## Heap
- **Description**: structure with `insert()`, `getmin()` and `extractmin()` operations
- **Creation**: O(log(N))
- **Search**: n/a
- **Insert**: O(log(N))
- **Delete**: n/a
- **getmin**: O(1)
- **extractmin**: O(log(N))
Min-heap is based on binary tree, root contains minimum (implementattion is
array-based).

## Binary search tree
- **Description**: binary tree with left son always < right son.
- **Creation**: O(Nlog(N))
- **Search**: O(log(N))
- **Insert**: O(log(N))
- **Delete**: O(log(N))
Complexity is for balanced tree. Implementation is list-based.

## Hash
- **Description**:
- **Creation**: O(N)
- **Search**: O(1)
- **Insert**: O(1)
- **Delete**: O(1)


# Summary
|Structure|Creation|Search|Insert|Delete|
|:---|    ---:|  ---:|  ---:|  ---:|
|Array|O(N)   |O(N)  |  O(N)|  O(N)|
|Stack|O(N)   |n/a   |  O(1)|  O(1)|
|List |O(N)   |O(N)  |  O(N)|  O(N)|
