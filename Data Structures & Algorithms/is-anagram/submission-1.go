func isAnagram(s string, t string) bool {

	if len(s) != len(t) {
		return false
	}
	
	sRunes, tRunes := []rune(s), []rune(t)

	sLessEqual := func(i, j int) bool {
		return sRunes[i] < sRunes[j]
	}

	tLessEqual := func(i, j int) bool {
		return tRunes[i] < tRunes[j]
	}

	sort.Slice(sRunes, sLessEqual)
	sort.Slice(tRunes, tLessEqual)
	for i, ch := range sRunes {
		if ch != tRunes[i] {
			return false
		}
	}
	return true
	
}
