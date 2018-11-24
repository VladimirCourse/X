import 'dart:convert';

class Topic {

  String topic;
  String destination;
  String origin;

  Topic({this.destination, this.origin, this.topic});

  factory Topic.fromJson(Map<String, dynamic> data){
    return Topic(
      topic: data['topic'],
      destination: data['destination'],
      origin: data['origin']
    );
  }
}