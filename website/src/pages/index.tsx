import { Button, Input, Stack } from "@chakra-ui/react";
import Head from "next/head";
import Link from "next/link";
import { useSession } from "next-auth/react";

import { CallToAction } from "src/components/CallToAction";
import { Faq } from "src/components/Faq";
import { Footer } from "src/components/Footer";
import { Header } from "src/components/Header";
import { Hero } from "src/components/Hero";

const Home = () => {
  const { data: session } = useSession();

  if (!session) {
    return (
      <>
        <Head>
          <title>Open Assistant</title>
          <meta
            name="description"
            content="Conversational AI for everyone. An open source project to create a chat enabled GPT LLM run by LAION and contributors around the world."
          />
        </Head>
        <Header />
        <main className="z-0">
          <Hero />
          <CallToAction />

          <Faq />
        </main>
        <Footer />
      </>
    );
  }
  return (
    <>
      <Head>
        <title>Open Assistant</title>
        <meta
          name="description"
          content="Conversational AI for everyone. An open source project to create a chat enabled GPT LLM run by LAION and contributors around the world."
        />
      </Head>
      <Header />
      <main className="h-3/4  z-0 bg-white flex flex-col items-center justify-center gap-2">
        <Button size="lg" colorScheme="blue" className="drop-shadow">
          <Link href="/evaluate/rate_summary">Rate a Summary</Link>
        </Button>
        <Button size="lg" colorScheme="blue" className="drop-shadow">
          <Link href="/create/summarize_story">Summarize a story</Link>
        </Button>
      </main>
      <Footer />
    </>
  );
};

export default Home;
