from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam

def create_model(input_number, output_number, learning_rate, kernel_initializer, bias_initializer):
    inputs = Input(shape=(input_number,))
    outputs = Dense(output_number, activation='linear',
                    kernel_initializer=kernel_initializer,
                    bias_initializer=bias_initializer,
                    use_bias=use_bias)(inputs)
    opt = Adam(learning_rate=learning_rate)
    loss = 'mean_squared_error'
    model = Model(inputs, outputs)
    model.compile(optimizer=opt, loss=loss, metrics=['mean_squared_error'])
    return model
