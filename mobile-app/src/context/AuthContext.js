import React, { createContext, useState, useEffect } from 'react';
import AsyncStorage from '@react-native-async-storage/async-storage';
import api from '../services/api';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [userToken, setUserToken] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  const login = async (username, password) => {
    try {
      const response = await api.post('/auth/login', { username, password });
      const token = response.data.access_token;
      setUserToken(token);
      await AsyncStorage.setItem('token', token);
      console.log('Login successful', token);
    } catch (e) {
      console.log('Login error', e);
      throw e;
    }
  };

  const signup = async (username, password, email) => {
    try {
      await api.post('/auth/register', { username, password, email });
      console.log('Signup successful');
    } catch (e) {
      console.log('Signup error', e);
      throw e;
    }
  };

  const logout = async () => {
    setUserToken(null);
    await AsyncStorage.removeItem('token');
  };

  const isLoggedIn = async () => {
    try {
      let token = await AsyncStorage.getItem('token');
      setUserToken(token);
    } catch (e) {
        console.log("Error checking token");
    } finally {
        setIsLoading(false);
    }
  }

  useEffect(() => {
    isLoggedIn();
  }, []);

  return (
    <AuthContext.Provider value={{ login, signup, logout, isLoading, userToken }}>
      {children}
    </AuthContext.Provider>
  );
};
