class LimitedQueue:

    def __init__(self, max_n):
        self.max_n = max_n
        self.queue = [None] * self.max_n
        self.head = 0  # Голова указывает на индекс 0
        self.tail = 0  # Хвост указывает на индекс 0
        self.size = 0  # При создании очередь пуста, её длина - 0

    def is_empty(self):
        return self.size == 0
  
    def push(self, value):
        if self.queue[self.tail] is not None:
            self.head = (self.head + 1) % self.max_n
        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.max_n
        if self.size < self.max_n:
            self.size += 1

# Начинаем проверку! Создаём очередь с ограничением 8 элементов:
q = LimitedQueue(8) 
q.push(1)  # Добавляем один элемент.
print('Очередь с одним элементом:', q.queue)
print('Длина очереди с одним элементом:', q.size)
# Добавляем ещё три элемента:
q.push(-1)
q.push(0)
q.push(11)
print('Очередь с четырьмя элементами:', q.queue)
print('Длина очереди с четырьмя элементами:',q.size)