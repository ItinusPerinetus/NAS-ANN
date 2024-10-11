from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam

def create_model(neurons, input_number = 10, output_number = 10, learning_rate = 0.001, kernel_initializer = 'glorot_uniform', bias_initializer = 'zeros'):
    inputs = Input(shape=(input_number,))
    x = Dense(neurons)(inputs)
    outputs = Dense(output_number, activation='linear',
                    kernel_initializer=kernel_initializer,
                    bias_initializer=bias_initializer,
                    use_bias=use_bias)(x)
    opt = Adam(learning_rate=learning_rate)
    loss = 'mean_squared_error'
    model = Model(inputs, outputs)
    model.compile(optimizer=opt, loss=loss, metrics=['mean_squared_error'])
    return model
