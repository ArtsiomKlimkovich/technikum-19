Funkcja CzyNalezy(a, n, T)
    lewy = 1
    prawy = n
    
    Podczas (lewy <= prawy)
        srodek = (lewy + prawy) // 2
        
        Jeśli T[srodek] == a wtedy
            Zwróć Prawda
        Inaczej jeśli T[srodek] < a wtedy
            lewy = srodek + 1
        Inaczej
            prawy = srodek - 1
            
    Zwróć Fałsz
