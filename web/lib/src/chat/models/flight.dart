import 'dart:convert';

class Flight {

  String origin;
  String destination;
  String departDate;
  String gate;
  double price;

  Flight({this.destination, this.origin, this.gate, this.departDate, this.price});

  factory Flight.fromJson(Map<String, dynamic> data){
    return Flight(
      departDate: data['depart_date'],
      destination: data['destination'],
      origin: data['origin'],
      price: data['price'].toDouble(),
      gate: data['gate']
    );
  }
}