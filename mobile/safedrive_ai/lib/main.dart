import 'package:flutter/material.dart';
import 'api.dart';

void main() => runApp(const MyApp());

class MyApp extends StatefulWidget {
  const MyApp({super.key});
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  double? score;
  String? error;
  bool loading = false;

  Future<void> callPredict() async {
    setState(() { loading = true; error = null; });
    try {
      final s = await SafeDriveApi.predict(
        temp: 25, precip: 0.3, vis: 3.5, hour: 18,
      );
      setState(() => score = s);
    } catch (e) {
      setState(() => error = e.toString());
    } finally {
      setState(() => loading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('SafeDriveAI – Demo')),
        body: Center(
          child: Column(mainAxisSize: MainAxisSize.min, children: [
            if (loading) const CircularProgressIndicator(),
            if (!loading && score != null) Text('Risk score: $score'),
            if (!loading && error != null) Text('Error: $error'),
            const SizedBox(height: 12),
            ElevatedButton(onPressed: callPredict, child: const Text('Call /predict')),
          ]),
        ),
      ),
    );
  }
}
