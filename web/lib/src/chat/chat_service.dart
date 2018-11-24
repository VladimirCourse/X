import 'dart:async';

import 'package:angular/core.dart';

import 'models/message.dart';

@Injectable()
class ChatService {
  List<Message> messages = [
    Message(isMy: false, message: 'kekeke'),
    Message(isMy: true, message: 'kekeke')
  ];

  Future<List<Message>> getMessages() async => messages;
}
