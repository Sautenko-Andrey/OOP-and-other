import numpy
import matplotlib.pyplot as plt
import scipy.special


# класс моей первой нейронной сети
class NeuralNetwork:

    # инициализация нейронной сети
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        '''Задание количество входных, скрытых и выходных узлов нейросети,
        а так же коэффициента обучения'''

        # слои
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # коэффициент обучения
        self.learning_rate = learning_rate

        # инициализация весовых коэффициентов (создание матриц весовых коэффициентов)
        self.weight_input_hidden = numpy.random.normal(0.0, pow(self.hidden_nodes, -0.5),
                                                       (self.hidden_nodes, self.input_nodes))
        self.weight_hidden_output = numpy.random.normal(0.0, pow(self.output_nodes, -0.5),
                                                        (self.output_nodes, self.hidden_nodes))

        # инициализация функции активации (сигмоиды)
        self.activation_function = lambda x: scipy.special.expit(x)

    # тренировка нейронной сети
    def train(self, inputs_list, targets_list):
        '''уточнение весовых коэффициентов в процессе
обработки предоставленных для обучения сети тренировочных
примеров'''
        # преобразуем списки входныx значений в двумерные массивы
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # рассчитаем входяхие сигналы для скрытого слоя
        hidden_input_signals = numpy.dot(self.weight_input_hidden, inputs)

        # расчитаем исходящие сигналы от скрытого слоя
        hidden_output_signals = self.activation_function(hidden_input_signals)

        # рассчитаем входящие сигналы для выходящего слоя
        final_input_signals = numpy.dot(self.weight_hidden_output, hidden_output_signals)

        # рассчитаем выходящие сигналы от выходящего слоя после функции активации
        final_output_signals = self.activation_function(final_input_signals)

        # ошибка = целевое значение - фактическое полученное
        errors = targets - final_output_signals

        # ошибки скрытого слоя являются ошибками error,
        # которые распределены пропорционально весовым коэффициентам связей
        # и рекомбинированные на скрытых узлах

        # рассчитаем расспространение ошибок для узлов скрытого слоя
        hidden_errors = numpy.dot(self.weight_hidden_output.T, errors)

        # рассчитаем расспространение ошибок для узлов входного слоя
        input_errors = numpy.dot(self.weight_input_hidden, hidden_errors)

        # обновляем весовые коэффициенты связей между скрытыми и выходными слоями
        self.weight_hidden_output += self.learning_rate * numpy.dot((errors * final_output_signals *
                                                                     (1 - final_output_signals)),
                                                                    numpy.transpose(hidden_output_signals))

        # обновляем весовые коэффициенты связей между скрытыми и входными слоями
        self.weight_input_hidden += self.learning_rate * numpy.dot((hidden_errors * hidden_output_signals *
                                                                    (1 - hidden_output_signals)),
                                                                   numpy.transpose(inputs))


    # опрос нейронной сети
    def query(self, input_signal_list):
        '''получение значений сигналов с выходных узлов после
предоставления значений входящих сигналов'''
        # преобразуем список входных сигналов в двумерный масив
        input_signals = numpy.array(input_signal_list, ndmin=2).T

        # получим входящие сигналы для узлов скрытого слоя
        hidden_input_signals = numpy.dot(self.weight_input_hidden, input_signals)

        # получим сигналы, выходящие из скрытого слоя после функции активации
        hidden_output_signals = self.activation_function(hidden_input_signals)

        # получим входящие сигналы для узлов выходного слоя
        final_input_signals = numpy.dot(self.weight_hidden_output, hidden_output_signals)

        # получим сигналы, выходящие из выходного слоя после функции активации
        final_output_signals = self.activation_function(final_input_signals)

        return final_output_signals


# пробы

# количество входных, скрытых и выходных узлов
input_nodes = 3
hidden_nodes = 3
output_nodes = 3

# коэффициент обучения
learning_rate = 0.3

# входящие сигналы
first_signal = 1
second_signal = 0.5
third_signal = -1.5

my_neural_network = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
my_neural_network.query([first_signal, second_signal, third_signal])
print(my_neural_network.query([first_signal, second_signal, third_signal]))
