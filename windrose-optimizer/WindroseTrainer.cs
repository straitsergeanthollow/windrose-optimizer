using System;
using System.Text.Json;

namespace WindroseOptimizer
{
    public class WindroseTrainer
    {
        private readonly TrainingConfig _config;

        public WindroseTrainer(TrainingConfig config)
        {
            _config = config;
        }

        public TrainingResult Train()
        {
            var rng = new Random();
            double bestAngle = 0;
            double bestScore = double.MinValue;

            for (int i = 0; i < _config.Epochs; i++)
            {
                double angle = rng.NextDouble() * 360;
                double score = Evaluate(angle);
                if (score > bestScore)
                {
                    bestScore = score;
                    bestAngle = angle;
                }
            }
            return new TrainingResult { BestAngle = bestAngle, Score = bestScore };
        }

        private double Evaluate(double angle)
        {
            // Simple optimization: prefer angles near 45° with some noise
            double target = 45.0;
            double diff = Math.Abs(angle - target);
            if (diff > 180) diff = 360 - diff;
            return 100.0 - diff + (new Random().NextDouble() - 0.5) * 10;
        }
    }

    public class TrainingResult
    {
        public double BestAngle { get; set; }
        public double Score { get; set; }

        public string ToJson()
        {
            return JsonSerializer.Serialize(this);
        }
    }
}