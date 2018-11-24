class Message {

  int id;

  bool isMy;

  String message;
  String messageType;
  String createdAt;

  dynamic data;

  Message({this.id, this.message, this.messageType, this.data, this.createdAt, this.isMy = false});

  factory Message.fromJson(Map<String, dynamic> json){
    var res = Message(
      id: json['id'],
      message: json['message'],
      messageType: json['message_type'],
      createdAt: json['created_at'],
      data: json['data']
    );

    return res;
  }

}