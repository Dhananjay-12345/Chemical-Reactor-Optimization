for temp in temperature:
    k = react1.rateconstant(temp)
    X1 = r1.conversion(k)
    X2 = r2.conversion(k)

    print()
    Cconversion_list.append(X1)
    Pconversion_list.append(X2)
    print(X1 , " " ,X2 , " ")