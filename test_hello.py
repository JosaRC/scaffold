from hello import add

def test_add():
    #arrange
    expect_value = 3
    
    #action
    actual = add(1,2)
    
    #assert
    assert expect_value == actual