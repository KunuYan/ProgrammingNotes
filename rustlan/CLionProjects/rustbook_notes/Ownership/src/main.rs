fn main() {
    let mut s = "ok";
    s = "ok2";
    s = s + " ok.. OK... ok";
println!("{}, boomer!", s);
}
// memory are store as in the stack or heap, or hardcoded program binary itself

// String types
// str: string literal
    // cannot be mutated, is hardcoded and stored as program binary
    // let mut s = "hello, world!";
    // s = "ok, OKEH BOOomER!"; you can do this
    // s = s + "nigguaaaH!"; can't do this since it requires ownership

// String
    //mutating, stored in the heap(exist in runtime only, stored in ram)
    // let s = String::from("hello"); have to create strings like this

// Utilizing the heap
// request memory from OS at runtime
    // String::from() // this method ask the os to allocate space in memory for our string
// return memory to OS once we are done
    // memory is automatically returned, when the object goes out of scope
    // other languages use a garbage collector, not rust

// _________________________________________________________________________________
// ways data and variables interact

fn data_interaction() {
    // this is possible because they are fixed size variables
    // stack-stored variables already have a copy trait
    // integers, bool, floats, char, tuples are stack-stored variables
    let x = 5; // bind 5 to x
    let y = x; // create a copy of x and bind it to y

    // there is no fixed size so ownership is required to deal with double free errors
    // are heap-stored(stored with a pointer, length and capacity) variables
    let s1 = String::from("hello");
    // s1 comes into scope
    let s2 = s1;
    // s2 comes into scope
    // pointer of s2 points to s1
}

fn ownership() {
    let s1 = String::from("hello");
    let s2 = s1;
    // the value of s1 is moved to s2(ownership is transferred), so s1 no longer has access to it.
    // if we want to copy data from one string to another and maintain both, we have to clone the original
    let s3 = s2.clone();
    // the heap data is being copy which is expensive on runtime performance.

    // some_fxn(s1); ownership of s1 is moved to the some_fxn()
    // s1 is no longer accessible from here till, some_fxn() returns it ownership


}
