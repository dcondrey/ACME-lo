class AdaptiveLearning:
    def __init__(self, parameter_count, learning_rate):
        self.parameters = [0.0] * parameter_count
        self.learning_rate = learning_rate

    def update_parameters(self, feedback):
        self.parameters = [p + self.learning_rate * f for p, f in zip(self.parameters, feedback)]

    def save_model_state(self, file_path):
        with open(file_path, 'w') as file:
            file.write(','.join(map(str, self.parameters)))

    def load_model_state(self, file_path):
        with open(file_path, 'r') as file:
            self.parameters = list(map(float, file.read().split(',')))

class ReinforcementLearning(AdaptiveLearning):
    def __init__(self, parameter_count, learning_rate):
        super().__init__(parameter_count, learning_rate)

    def learn_from_environment(self, state, action, reward):
        feedback = self.calculate_feedback(state, action, reward)
        self.update_parameters(feedback)

    def choose_action(self, state):
        action_values = [sum(s * p for s, p in zip(state, self.parameters))]
        return action_values.index(max(action_values))

    def calculate_feedback(self, state, action, reward):
        predicted_reward = sum(state[i] * self.parameters[i] for i in range(len(state)))
        feedback = [0.0] * len(self.parameters)
        feedback[action] = reward - predicted_reward
        return feedback

class SupervisedLearning(AdaptiveLearning):
    def __init__(self, parameter_count, learning_rate):
        super().__init__(parameter_count, learning_rate)

    def train(self, input_data, expected_output):
        prediction = self.make_prediction(input_data)
        feedback = [expected - pred for expected, pred in zip(expected_output, prediction)]
        self.update_parameters(feedback)

    def make_prediction(self, input_data):
        return [sum(inp * p for inp, p in zip(input_data, self.parameters))]

