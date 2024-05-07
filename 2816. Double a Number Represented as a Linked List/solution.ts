/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */

class ListNode {
    val: number
    next: ListNode | null
    constructor(val?: number, next?: ListNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.next = (next===undefined ? null : next)
    }
}

function getStringRepresentation(node: ListNode | null) :string {
    if(!node) return "";
    if(!node.next) return `${node.val}`;
    return `${node.val}` + getStringRepresentation(node.next)
}

function doubleIt(head: ListNode | null): ListNode | null {
    if(head) {

        // accumulate numbers as a string
        let stringRepresentation :string = getStringRepresentation(head);

        // convert stringified number to BigInt, double it, then convert it back to an array of chars
        const doubled :BigInt = BigInt(stringRepresentation) * 2n;
        const arrayRepresentation :string[] = `${doubled}`.split("");

        // create a new linked list with submission
        let newHead: ListNode = new ListNode(parseInt(arrayRepresentation[0]));
        let prev: ListNode = newHead;
        for(let i = 1; i < arrayRepresentation.length; i++) {
            const newNode : ListNode = new ListNode(parseInt(arrayRepresentation[i]));
            prev.next = newNode;
            prev = newNode;
        }

        return newHead;
    }

    return null;
};
