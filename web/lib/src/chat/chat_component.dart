import 'dart:async';

import 'package:angular/angular.dart';
import 'package:angular_components/angular_components.dart';

import 'chat_service.dart';

import 'models/message.dart';

@Component(
  selector: 'chat',
  styleUrls: ['chat_component.css'],
  templateUrl: 'chat_component.html',
  directives: [
    MaterialCheckboxComponent,
    MaterialFabComponent,
    MaterialIconComponent,
    materialInputDirectives,
    NgFor,
    NgIf,
  ],
  providers: [const ClassProvider(ChatService)],
)
class ChatComponent implements OnInit {
  final ChatService  messageService;

  String message;

  List<Message> items = [];

  ChatComponent(this.messageService);

  @override
  Future<Null> ngOnInit() async {
    items = await messageService.getMessages();
  }

  void add(String msg) {
    items.add(Message(message: msg, isMy: true));
    message = '';
  }
}
