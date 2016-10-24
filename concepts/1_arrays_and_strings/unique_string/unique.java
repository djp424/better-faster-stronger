public class unique {

	public static void main(String[] args) {
		System.out.println(is_unique( "abcdefghijklmnopqrstuvwxyz" )); // true
		System.out.println(is_unique( "abcdefghijklmnopqrstuvwxyzz" )); // false
		System.out.println(is_unique( "aa" )); // false
		System.out.println(is_unique( "aba" )); // false
		System.out.println(is_unique( "aaaaaaaaaaaaaaaaaaaaaaaaaaa" )); // false
		System.out.println(is_unique( "  " )); // false
		System.out.println(is_unique( " " )); // true
	}

	public static boolean is_unique(String str) {
		if (str.length() > 128) { // assume ascii, not unicode
			return false;
		}

		boolean[] alf = new boolean[128];
		for (int i = 0; i < str.length(); i++) {
			int val = str.charAt(i);
			if (alf[val]) {
				return false;
			}
			alf[val] = true;
		}
		return true;
	}

}
