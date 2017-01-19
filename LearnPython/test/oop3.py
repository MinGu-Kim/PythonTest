'''
init 메소드 : 객체가 생성될 때 여러가지 초기화작업을 할 때
					유용하게 사용할 수 있다. 메소드명은 '__init__'

파이썬의 클래스는 여러가지 특별한 메소드가 존재한다.
그중에서 init 메소드는 클래스가 인스턴스화(객체화) 될 때 호출된다.
'''

class Person:
    def __init__(self, name):
        self.name = name
    def say(self):
        print("저의 이름은",self.name)

p1 = Person("김민구")
p1.say()

'''
 필드는 일반적인 변수와 똑같다. 한가지 차이점이 있다면 네임스페이스에 묶여있다라는 점이다.
 필드는 해당 클래스 또는 객체 내부에서만 의미가 있다.
 해당 클래스 내부와 객체 내부를 네임스페이스라고 한다.
 다시 얘기해서 필드가 통용되는 공간(필드 내부, 객체 내부)을 의미한다.

 필드에는 클래스 변수가 있고, 객체 변수가 있다.
 (필드를 소유하고 있는 대상이 클래스이냐, 객체이냐에 따라서 클래스변수, 객체변수로 구별된다.)

 클래스 변수는 공유된다. (다시 얘기해서, 클래스로 부터 생성된 모든 인스턴스들이 접근할 수 있다)
 클래스 변수는 하나만 존재한다. 어떤 객체가 클래스 변수를 변경한다면
 다른 인스턴스들에게도 변경내용이 반영된다.

 객체변수(인스턴스변수)는 클래스로부터 생성된 각각의 객체(인스턴스)에 속해 있는 변수
 객체별로 객체 변수를 하나씩 따로 가지고 있다. 즉, 서로 공유하지 않는다.

'''