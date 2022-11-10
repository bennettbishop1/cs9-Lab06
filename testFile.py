#testFile.py
from Apartment import Apartment
from lab06 import *

def test___gt__():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(1000, 0, "bad")
    a5 = Apartment(900, 0, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert (a0 > a1) == True
    assert (a0 > a5) == True
    assert (a5 > a0) == False

def test___lt__():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(0, 0, "bad")
    a5 = Apartment(0, 0, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert (a0 > a1) == True
    assert (a0 > a5) == True
    assert (a5 > a0) == False

def test_getApartmentDetails():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(0, 0, "bad")
    a5 = Apartment(0, 0, "bad")
    a = [a0, a1, a2, a3, a4, a5]

    assert a0.getApartmentDetails() == '(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad'
    assert a4.getApartmentDetails() == '(Apartment) Rent: $0, Distance From UCSB: 0m, Condition: bad'

def test___eq__():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 215, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(0, 0, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]

    assert (a2 == a3) == True
    assert (a0 == a1) == False

def test_mergesort():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 215, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(0, 0, "bad")
    a = [a0, a1, a2, a3, a4, a5]
    mergesort(a)
    expected = [a5, a4, a3, a2, a1, a0]
    for i in range(len(a)):
        assert expected[i] == a[i]

def test_ensureSortedAscending():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 215, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(0, 0, "bad")
    a = [a0, a1, a2, a3, a4, a5]
    expected = [a5, a4, a3, a2, a1, a0]
    assert ensureSortedAscending(a) == False
    assert ensureSortedAscending(expected) == True
    
def test_getBestApartment():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 215, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(0, 0, "bad")
    a = [a0, a1, a2, a3, a4, a5]
    expected = [a5, a4, a3, a2, a1, a0]
    assert getBestApartment(a) == '(Apartment) Rent: $0, Distance From UCSB: 0m, Condition: bad'
    assert (getBestApartment(a) == '(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent') == False
    
def test_getWorstApartment():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 215, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(0, 0, "bad")
    a = [a0, a1, a2, a3, a4, a5]
    expected = [a5, a4, a3, a2, a1, a0]
    assert getWorstApartment(a) == '(Apartment) Rent: $1115, Distance From UCSB: 215m, Condition: bad'
    assert (getWorstApartment(a) == '(Apartment) Rent: $0, Distance From UCSB: 0m, Condition: bad') == False

def test_getAffordableApartments():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 215, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(0, 0, "bad")
    a = [a0, a1, a2, a3, a4, a5]
    expected = '(Apartment) Rent: $0, Distance From UCSB: 0m, Condition: bad\n(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent'
    result = getAffordableApartments(a, 900)
    assert expected == result
    result = getAffordableApartments(a, 975)
    expected = '(Apartment) Rent: $0, Distance From UCSB: 0m, Condition: bad\n(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent\n(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: excellent\n(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: excellent\n(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average'
    assert expected == result