import React, { useEffect, useState } from 'react';
import { View, StyleSheet, ActivityIndicator, Text } from 'react-native';
import { Video, ResizeMode } from 'expo-av';
import api from '../services/api';

const PlayerScreen = ({ route }) => {
  const { videoId } = route.params;
  const [videoUrl, setVideoUrl] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchStreamUrl();
  }, []);

  const fetchStreamUrl = async () => {
    try {
        const response = await api.get(`/video/${videoId}/stream`);
        if (response.data.stream_url) {
            setVideoUrl(response.data.stream_url);
        }
    } catch (e) {
        console.log("Error fetching stream", e);
    } finally {
        setLoading(false);
    }
  };

  if (loading) {
      return (
          <View style={styles.container}>
              <ActivityIndicator size="large" color="#0000ff" />
          </View>
      );
  }

  if (!videoUrl) {
      return (
          <View style={styles.container}>
              <Text>Failed to load video.</Text>
          </View>
      )
  }

  return (
    <View style={styles.container}>
      <Video
        style={styles.video}
        source={{
          uri: videoUrl,
        }}
        useNativeControls
        resizeMode={ResizeMode.CONTAIN}
        isLooping
        shouldPlay
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: 'black',
    justifyContent: 'center',
    alignItems: 'center',
  },
  video: {
    width: '100%',
    height: 300,
  },
});

export default PlayerScreen;
