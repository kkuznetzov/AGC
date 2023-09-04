#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu August 31 08:06:00 2023

@author: kkn
"""

from os.path import dirname, join as pjoin
from scipy.io import wavfile
import pdb
import scipy.io
import math
import random
import matplotlib.pyplot as plt
import numpy as np
import os

# Input wav file
# Имя входного wav файла
input_wav_file_name = 'wav\\test_signal_out.wav'
input_wav_file_name = os.path.join(os.path.dirname(__file__), input_wav_file_name)

# Input wav file
# Имя входного wav файла
output_wav_file_name = 'wav\\agc_signal_out.wav'
output_wav_file_name = os.path.join(os.path.dirname(__file__), output_wav_file_name)

# Sampling rate of wav file, other values don't work
# Частота дискретизации файла wav
wav_samplerate = 44100

# Automatic Gain Control Coefficients
# Desired gain R from 0 to 1
# Параметры автоматической регулировки усиления
# Желаемое усиление R от 0 до 1
agc_desired_gain = 1

# Filter length
# Длина фильтра
average_buffer_size = 100
average_buffer_counter = 0
average_buffer = np.linspace(agc_desired_gain, agc_desired_gain, int(average_buffer_size))
average_value = 0

# Open wav file for reading
# Читаем входной файл
input_signal_samplerate, input_signal_data = wavfile.read(input_wav_file_name)
input_signal_length = input_signal_data.shape[0]

# Scale the samples of the input signal so that they are in the range from -1 to 1
# Масштабируем входной сигнал, что бы максимум был 1 или -1
input_signal_maximum_amplitude = max(abs(input_signal_data))
input_signal_data = input_signal_data / input_signal_maximum_amplitude

# Form the output signal
# Формируем выходной сигнал
output_signal_data = np.linspace(0, 0, int(input_signal_length))

# Loop through input samples
# Проход по входным отсчётам
for i in range(int(input_signal_length)):
    # Реализация автоматического регулирования усиления
    # Implementing Automatic GainControl

    # Floating Average Filter
    # Фильтр плавающего среднего
    average_buffer[average_buffer_counter] = abs(input_signal_data[i])
    average_value = np.mean(average_buffer)

    # Calculate gain value
    # Вычисление значения усиления
    gain_value = agc_desired_gain / average_value

    # Multiply the signal by the gain
    # Умножаем сигнал на усиление
    output_signal_data[i] = input_signal_data[i] * gain_value

    # Floating average buffer counter increment
    # Инкремент счётчика буфера плавающего среднего
    average_buffer_counter += 1
    if average_buffer_counter >= average_buffer_size:
        average_buffer_counter = 0

# Scale the samples of the output signal so that they are in the range from -1 to 1
# Масштабируем выходной сигнал, что бы максимум был 1 или -1
output_signal_maximum_amplitude = max(abs(output_signal_data))
output_signal_data = output_signal_data / output_signal_maximum_amplitude

# Save wav file
# Сохраним в файл
output_signal_data *= 32765
output_signal_int = np.int16(output_signal_data)
wavfile.write(output_wav_file_name, wav_samplerate, output_signal_int)
