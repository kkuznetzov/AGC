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

# Output audio file with signal
# Имя выходного wav файла
wav_file_name = 'wav\\test_signal_out.wav'
wav_file_name = os.path.join(os.path.dirname(__file__), wav_file_name)

# Sampling rate of wav file, other values don't work
# Частота дискретизации файла wav
wav_samplerate = 44100

# Signal frequency
# Значение частоты сигнала
signal_frequency = 1000

# Signal duration, second
# Длительность сигнала, секунд
signal_duration = 1

# Modulation frequency
# Частота модуляции
modulation_frequency = 10

# Modulation index, 0 to 1
# Индекс модуляции, от 0 до 1
modulation_index = 0.5

# Number of signal samples
# Число отсчётов сигнала
signal_samples = signal_duration * wav_samplerate

# Generation of signal samples
# Генерация отсчётов сигнала
signal_samples_index = np.arange(signal_samples)
output_signal = np.cos(2 * np.pi * signal_frequency * signal_samples_index / signal_samples)

# Generation of samples of the modulation signal
# Генерация отсчётов сигнала модуляции
modulation_signal = np.cos(2 * np.pi * modulation_frequency * signal_samples_index / signal_samples)

# Multiplying Signals
# Перемножаем сигналы
output_signal = output_signal * (1 + modulation_index * modulation_signal) / (1 + modulation_index)

# Save wav file
# Сохраним в файл
output_signal *= 32765
output_signal_int = np.int16(output_signal)
wavfile.write(wav_file_name, wav_samplerate, output_signal_int)


