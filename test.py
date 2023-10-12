from main import Insaan

insaan = Insaan()
def defaultNameTest():
    assert insaan.getName() == "Default"

def defaultAgeTest():
    assert insaan.getAge() == 0
    
def setNameTest():
    insaan.setName("shareef")
    assert insaan.getName() == "shareef"
    
def setAgeTest():
    insaan.setAge(20)
    assert insaan.getAge() == 20