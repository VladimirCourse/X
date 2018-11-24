class Message {

  int id;

  bool isMy;

  String message;
  DateTime createdAt;

  Message({this.id, this.message, this.createdAt, this.isMy = false});

}