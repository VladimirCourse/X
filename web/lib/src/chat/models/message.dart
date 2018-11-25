class Message {

  int id;

  String message;
  String messageType;
  String user;
  String createdAt;

  dynamic data;

  Message({this.id, this.message, this.messageType, this.data, this.createdAt, this.user});

  factory Message.fromJson(Map<String, dynamic> json){
    var res = Message(
      id: json['id'],
      message: json['message'],
      messageType: json['messageType'],
      createdAt: json['createdAt'],
      data: json['data'],
      user: json['user']
    );

    return res;
  }

}