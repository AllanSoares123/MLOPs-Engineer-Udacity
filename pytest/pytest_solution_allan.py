1. **Escreva um teste simples**
   Escreva uma função chamada add que aceita dois números e retorna a soma deles. Em seguida, escreva um teste usando Pytest para verificar se a função está funcionando corretamente.
python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5

2. **Teste uma exceção**
   Escreva uma função chamada divide que aceita dois números e retorna a divisão do primeiro pelo segundo. A função deve lançar uma exceção ValueError se o segundo número for zero. Escreva um teste para verificar se a exceção é lançada corretamente.
python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide():
    with pytest.raises(ValueError):
        divide(1, 0)

3. **Use fixtures**
   Pytest fixtures são funções que são executadas antes de cada teste. Eles são usados para configurar o estado do teste. Escreva uma fixture que retorna uma lista de números e um teste que verifica se a soma dos números na lista é correta.
python
@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]

def test_sum(numbers):
    assert sum(numbers) == 15

4. **Use parametrize**
   Pytest permite que você execute um teste com diferentes conjuntos de parâmetros usando a função parametrize. Escreva um teste para a função add que verifica se ela funciona corretamente para diferentes conjuntos de números.
python
@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (4, 5, 9), (7, 8, 15)])
def test_add(a, b, expected):
    assert add(a, b) == expected

5. **Teste uma classe**
   Crie uma classe Person com um método greet que retorna uma saudação personalizada. Escreva um teste para verificar se o método greet está funcionando corretamente.
python
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"

def test_person_greet():
    person = Person("Allan")
    assert person.greet() == "Hello"

6. **Use a fixture de solicitação**
   A fixture de solicitação do Pytest permite que você acesse informações sobre o teste atual. Use a fixture de solicitação para imprimir o nome do teste atual.
python
def test_request(request):
    print(f"Running test: {request.node.name}")

7. **Teste um método que altera o estado do objeto**
   Adicione um método set_name à classe Person que altera o nome da pessoa. Escreva um teste para verificar se o método set_name está funcionando corretamente.
python
class Person:
    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

def test_person_set_name():
    person = Person("Allan")
    person.set_name("Soares")
    assert person.name == "Soares"

8. **Use a fixture de módulo**
   A fixture de módulo do Pytest é executada uma vez por módulo. Use a fixture de módulo para configurar um estado que é compartilhado entre vários testes.
python
@pytest.fixture(scope="module")
def shared_state():
    return {"value": 0}

def test_shared_state_1(shared_state):
    shared_state["value"] += 1
    assert shared_state["value"] == 1

def test_shared_state_2(shared_state):
    assert shared_state["value"] == 1


