import 'dart:convert';

class Topic {

  String topic;
  String destination;
  String origin;
  String weatherSuggestion;
  String weatherTemp;

  Topic({this.destination, this.origin, this.topic, this.weatherSuggestion, this.weatherTemp});

  factory Topic.fromJson(Map<String, dynamic> data){
    return Topic(
      topic: data['topic'],
      destination: data['destination'],
      origin: data['origin'],
      weatherSuggestion: data['weatherSuggestion'],
      weatherTemp: data['weatherTemp'],
    );
  }
}