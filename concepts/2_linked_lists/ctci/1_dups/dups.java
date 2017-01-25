import java.util.*;

public class dups {
	public static void deleteDups( LinkedList ll ) {
		HashSet<String> set = new HashSet<String>();

		for (int i = 0; i < ll.size(); i = i + 1) {
			String currentData = ll.get( i ).toString();
			if (set.contains(currentData)) {
				ll.remove(i);
				System.out.println("Removed Dup: " + currentData);
			} else {
				set.add(currentData);
			}
		}

	}

	public static void main(String args[]) {
		LinkedList<String> ll = new LinkedList<String>(); // You should use <String> here

		ll.add("J");
		ll.add("J");
		ll.add("U");
		ll.add("S");
		ll.add("T");
		ll.add("3");
		ll.add("I");
		ll.add("C");
		ll.add("E");
		ll.add("3");
		System.out.println("Before: " + ll);

		deleteDups(ll);

		System.out.println("After: " + ll);
	}
}
