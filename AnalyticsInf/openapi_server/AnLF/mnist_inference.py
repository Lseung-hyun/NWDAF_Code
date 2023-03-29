import tensorflow as tf
import timeit


def inference():
    start_time = timeit.default_timer()
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    # 각종 파라메터의 영향을 보기 위해 랜덤값 고정
    tf.random.set_seed(1234)

    # Normalizing data
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # (60000, 28, 28) => (60000, 28, 28, 1)로 reshape
    x_train = x_train.reshape(-1, 28, 28, 1)
    x_test = x_test.reshape(-1, 28, 28, 1)

    # One-hot 인코딩
    y_train = tf.keras.utils.to_categorical(y_train, 10)
    y_test = tf.keras.utils.to_categorical(y_test, 10)

    # 모델 복원

    loaded_model = tf.keras.models.load_model('/home/nwdaf/5GC_APIs_NWDAF/AnalyticsInf/openapi_server/AnLF/models/mnist_1.h5')
    loaded_model.summary()

    result = loaded_model.evaluate(x_test, y_test)

    end_time = timeit.default_timer()

    return(result[1]*100)

#    Inference_time = end_time - start_time