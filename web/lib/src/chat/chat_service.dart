import 'dart:async';
import 'dart:io';
import 'dart:convert';

import 'package:http/http.dart' as http;

import 'package:angular/core.dart';

import 'models/message.dart';
import 'models/topic.dart';
import 'models/place.dart';
import 'models/flight.dart';

@Injectable()
class ChatService {

  static const String msgUrl = 'http://localhost:5000/message';
  static const String topicUrl = 'http://localhost:5000/topic';
  static const String flightUrl = 'http://localhost:5000/flight';
  static const String hotelUrl = 'http://localhost:5000/hotel';
  static const String messagesUrl = 'http://localhost:5000/messages';
  static const String placesUrl = 'http://localhost:5000/places';

  Future<Message> sendMessage(String msg) async {
    var res = await http.post(msgUrl,
      headers: {
        'Content-Type': 'application/json'
      },
      body: json.encode({
        'message': msg
      }),
    );
    if (res.statusCode == HttpStatus.ok){
      return Message.fromJson(json.decode(res.body));
    } 
  }

  Future<Topic> getTopic() async {
    var res = await http.get(topicUrl,
      headers: {
        'Content-Type': 'application/json'
      },
    );
    if (res.statusCode == HttpStatus.ok){
      return Topic.fromJson(json.decode(res.body));
    } 
  }

  Future<Flight> getFlight() async {
    var res = await http.get(flightUrl,
      headers: {
        'Content-Type': 'application/json'
      },
    );
    if (res.statusCode == HttpStatus.ok){
      return Flight.fromJson(json.decode(res.body));
    } 
  }

  Future<Place> getHotel() async {
    var res = await http.get(hotelUrl,
      headers: {
        'Content-Type': 'application/json'
      },
    );
    if (res.statusCode == HttpStatus.ok){
      return Place.fromJson(json.decode(res.body));
    } 
  }

  Future<List<Message>> getMessages() async {
    var res = await http.get(messagesUrl,
      headers: {
        'Content-Type': 'application/json'
      },
    );
    if (res.statusCode == HttpStatus.ok){
      return json.decode(res.body).map<Message>((p) => Message.fromJson(p)).toList();
    } 
  }

  Future<List<Place>> getPlaces() async {
    var res = await http.get(placesUrl,
      headers: {
        'Content-Type': 'application/json'
      },
    );
    if (res.statusCode == HttpStatus.ok){
      return json.decode(res.body).map<Place>((p) => Place.fromJson(p)).toList();
    } 
  }
}
