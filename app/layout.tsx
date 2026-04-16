import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Titanic Survival Predictor",
  description: "A colorful, lightweight Titanic survival prediction app for Vercel.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}