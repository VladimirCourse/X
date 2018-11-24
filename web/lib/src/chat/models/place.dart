import 'dart:convert';

class Place {

  String name;
  String address;
  String category;

  int price;

  Place({this.name, this.address, this.category, this.price});

  factory Place.fromJson(Map<String, dynamic> data){
    return Place(
      name: data['name'],
      address: data['address'],
      category: data['category'],
      price: data['price']
    );
  }
}