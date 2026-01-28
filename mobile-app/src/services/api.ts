import axios from 'axios';
import AsyncStorage from '@react-native-async-storage/async-storage';

// Replace with your actual local IP or emulator IP
// Android Emulator: 10.0.2.2
// iOS Simulator: localhost
// Physical Device: Your generic local IP
const API_URL = 'http://10.253.174.1:5000'; 

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use(
  async (config) => {
    const token = await AsyncStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default api;
