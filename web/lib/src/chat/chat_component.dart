import 'dart:async';

import 'package:angular/angular.dart';
import 'package:angular_components/angular_components.dart';

import 'chat_service.dart';

import 'models/message.dart';
import 'models/flight.dart';
import 'models/topic.dart';

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
    NgClass
  ],
  providers: [const ClassProvider(ChatService)],
)

class ChatComponent implements OnInit {
  final ChatService  messageService;

  String message;

  List<Message> messages = [];

  Flight flight;
  Topic topic = Topic();

  ChatComponent(this.messageService);

  @override
  Future<Null> ngOnInit() async {
    topic = await messageService.getTopic();
    messages = await messageService.getMessages();
  }

  void add(String msg) async {
    messages.add(Message(message: msg, isMy: true));
    var res = await messageService.sendMessage(msg);
    topic = await messageService.getTopic();
    if (res != null){ 
      if (res.messageType == 'flights_from' || res.messageType == 'flights_to'){
        flight = Flight.fromJson(res.data);
      }
    }

    message = '';
  }
}
