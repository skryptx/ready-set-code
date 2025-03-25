# Web Workers
1. Web workers are used to run resource intensive operations without blocking the main thread.\
```Class used: Worker```
2. They dont have access to DOM.
3. Workers run in a separate global context, so you ```cannot use certain objects like window, document, or parent```.
4. Use transferrable objects when passing the data:\
    How to Use Transferable Objects:\

    ### In Main program:
    Create a transferable object such as an ArrayBuffer:
    ```js
    const buffer = new ArrayBuffer(1024); // Create a buffer
    worker.postMessage(buffer, [buffer]); // Transfer ownership to worker
    ```

    ### In the Worker:

    Accept ownership and process the data:
    
    ```js
    self.onmessage = function(event) {
        const transferredBuffer = event.data;
        // Use the buffer without copying
    };
    ```

    Be mindful that once transferred, the main thread no longer retains ownership of the object. If additional use is required, make copies before transferring.

5. Details explained here: https://www.youtube.com/watch?v=fh2rKs7eupg
