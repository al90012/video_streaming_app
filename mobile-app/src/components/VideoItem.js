import React from 'react';
import { View, Text, Image, TouchableOpacity, StyleSheet } from 'react-native';

const VideoItem = ({ video, onPress }) => {
  return (
    <TouchableOpacity style={styles.container} onPress={onPress}>
      <Image source={{ uri: video.thumbnail_url }} style={styles.thumbnail} />
      <View style={styles.info}>
        <Text style={styles.title}>{video.title}</Text>
      </View>
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  container: {
    marginBottom: 20,
    borderRadius: 10,
    overflow: 'hidden',
    backgroundColor: '#f9f9f9',
    elevation: 3,
  },
  thumbnail: {
    width: '100%',
    height: 200,
  },
  info: {
    padding: 10,
  },
  title: {
    fontSize: 16,
    fontWeight: 'bold',
  },
});

export default VideoItem;
