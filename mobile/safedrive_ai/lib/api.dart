import 'dart:convert';
import 'package:http/http.dart' as http;

class SafeDriveApi {
  // From Android emulator to your PC's localhost:
  static const base = "http://10.0.2.2:8000";

  static Future<double> predict({
    required double temp,
    required double precip,
    required double vis,
    required int hour,
  }) async {
    final r = await http.post(
      Uri.parse("$base/predict"),
      headers: {"Content-Type": "application/json"},
      body: jsonEncode({
        "temperature": temp,
        "precipitation": precip,
        "visibility": vis,
        "hour": hour
      }),
    );
    if (r.statusCode != 200) {
      throw Exception("API error ${r.statusCode}: ${r.body}");
    }
    return (jsonDecode(r.body)["risk_score"] as num).toDouble();
  }
}
