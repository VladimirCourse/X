import 'dart:async';

import 'package:angular/angular.dart';
import 'package:angular_components/angular_components.dart';

import 'chat_service.dart';

import 'models/message.dart';
import 'models/flight.dart';
import 'models/topic.dart';
import 'models/place.dart';

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
  Place hotel;
  Topic topic = Topic();
  List<Place> places;
  List<Place> food;

  ChatComponent(this.messageService); 

  @override
  Future<Null> ngOnInit() async {
    topic = await messageService.getTopic();
    messages = await messageService.getMessages();
    flight = await messageService.getFlight();
    hotel = await messageService.getHotel();
    places = await messageService.getPlaces();
    food = await messageService.getFood();

    Timer.periodic(Duration(seconds: 1), 
      (timer) async{
        messages = await messageService.getMessages();  
      }
    );
  }

  void add(String msg) async {
    messages.add(Message(message: msg, messageType: 'my_message'));
    var res = await messageService.sendMessage(msg);
    print(res.messageType);
    if (res != null){ 
      if (res.messageType == 'flights_from' || res.messageType == 'flights_to'){
        if (flight != null){
          hotel = await messageService.getHotel();
          places = await messageService.getPlaces();
        }
        flight = Flight.fromJson(res.data);
      } else if (res.messageType == 'hotel'){
        hotel = Place.fromJson(res.data);
      } else if (res.messageType == 'places'){
        places = res.data.map<Place>((p) => Place.fromJson(p)).toList();
      } else if (res.messageType == 'food'){
        food = res.data.map<Place>((p) => Place.fromJson(p)).toList();
      }
    }

    topic = await messageService.getTopic();

    message = '';
  }
}
