import React, { useEffect, useState, useContext } from 'react';
import { View, FlatList, StyleSheet, Button, Text } from 'react-native';
import api from '../services/api';
import VideoItem from '../components/VideoItem';
import { AuthContext } from '../context/AuthContext';

const DashboardScreen = ({ navigation }) => {
  const [videos, setVideos] = useState([]);
  const { logout } = useContext(AuthContext);

  useEffect(() => {
    fetchVideos();
  }, []);

  const fetchVideos = async () => {
    try {
        const response = await api.get('/dashboard/');
        setVideos(response.data);
    } catch (e) {
        console.log("Error fetching videos", e);
    }
  };

  const renderItem = ({ item }) => (
    <VideoItem 
        video={item} 
        onPress={() => navigation.navigate('Player', { videoId: item.id })} 
    />
  );

  return (
    <View style={styles.container}>
      <FlatList
        data={videos}
        keyExtractor={(item) => item.id}
        renderItem={renderItem}
        contentContainerStyle={styles.list}
      />
      <Button title="Logout" onPress={logout} color="red" />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  list: {
    padding: 10,
  },
});

export default DashboardScreen;
