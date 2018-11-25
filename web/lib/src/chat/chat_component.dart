import 'dart:async';

import 'package:angular/angular.dart';
import 'package:angular_components/angular_components.dart';
import 'package:intl/intl.dart';

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

  int sum = 0;

  ChatComponent(this.messageService); 

  void calcsum(){
    sum = 0;
    if (flight != null){
      sum += flight.price.toInt();
    }
    if (hotel != null){
      sum += hotel.price.toInt() * 7;
    }
  }

  @override
  Future<Null> ngOnInit() async {
    topic = await messageService.getTopic();
    messages = await messageService.getMessages();
    flight = await messageService.getFlight();
    hotel = await messageService.getHotel();
    places = await messageService.getPlaces();
    food = await messageService.getFood();

    Timer.periodic(Duration(seconds: 1), 
      (timer) async {
        var tmp = await messageService.getMessages();  
        if (tmp.length > messages.length){
          messages = tmp;
          topic = await messageService.getTopic();
          flight = await messageService.getFlight();
          hotel = await messageService.getHotel();
          places = await messageService.getPlaces();
          food = await messageService.getFood();
        }
      }
    );
    calcsum();
  }

  void add(String msg) async {
    messages.add(Message(message: msg, messageType: 'my_message', user: 'user1', createdAt: DateFormat('hh:mm').format(DateTime.now())));
    var res = await messageService.sendMessage(msg, 'user1');
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

    calcsum();

    topic = await messageService.getTopic();

    message = '';
  }
}
