from islice_lib import my_islice_generator, my_islice_iterator

def test_my_isslice_generator () :
    print("isslice generator")    
    
    assert list(my_islice_generator('', 2, 5))             == [] 
    assert list(my_islice_generator('ABCDEFG', 2, 5))      == ['C', 'D', 'E'] 
    assert list(my_islice_generator('ABCDEFG', 2, 7))      == ['C', 'D', 'E', 'F', 'G'] 
    

def test_my_isslice_iterator1 () :
    print("isslice iterator")   

    p = my_islice_iterator('', 2, 5)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p
    assert list(p) == []
    
    
def test_my_isslice_iterator2 () :
    print("isslice iterator") 
      
    p = my_islice_iterator('ABCDEFG', 2, 5)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p
    assert list(p) == ['C', 'D', 'E'] 
    
def test_my_isslice_iterator3 () :
    print("isslice iterator")   

    p = my_islice_iterator('ABCDEFG', 2, 7)
    assert hasattr(p, "__iter__")
    assert hasattr(p, "__next__")
    q = iter(p)
    assert q is p
    assert list(p) == ['C', 'D', 'E', 'F', 'G'] 