func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	maps, mapt := make(map[rune]int), make(map[rune]int)
	for i, ch := range s {
		maps[ch]++
		mapt[rune(t[i])] ++
	}

	for k,v := range maps {
		if mapt[k] != v{
			return false;
		}
	}

	return true;
	
	
	
}
