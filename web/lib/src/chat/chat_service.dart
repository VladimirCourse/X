import 'dart:async';
import 'dart:io';
import 'dart:convert';

import 'package:http/http.dart' as http;

import 'package:angular/core.dart';

import 'models/message.dart';
import 'models/topic.dart';

@Injectable()
class ChatService {

  static const String msgUrl = 'http://localhost:5000/message';
  static const String topicUrl = 'http://localhost:5000/topic';

  List<Message> messages = [
  ];

  Future<List<Message>> getMessages() async => messages;

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
}
