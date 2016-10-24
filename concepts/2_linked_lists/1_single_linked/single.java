import java.util.*;

public class single {
	public static void main(String args[]) {
		LinkedList<String> ll = new LinkedList<String>(); // You should use <String> here

		// add
		ll.add("J");
		ll.add("U");
		ll.add("S");
		ll.add("T");
		ll.add("I");
		ll.add("C");
		ll.add("E");
		ll.addLast("Parsons");
		ll.addFirst("David");
		ll.add(1, "to the");
		ll.addLast("III");
		ll.addLast("III");
		System.out.println("Linked List after add: " + ll);

		// remove
		ll.remove("III"); // this only removes one of the III node's above
		ll.remove(1); // remove from position 1 (the second node)
		System.out.println("Linked List after remove: " + ll);

		// remove first and last
		ll.removeFirst();
		ll.removeLast();
		System.out.println("Linked List after removing first and last: " + ll);

		// get and set a value
		Object temp = ll.get(2);
		ll.set(2, (String) temp + " is same same but different but still same");
		System.out.println("Linked List after changing second element: " + ll);
	}
}
